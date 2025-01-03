from abc import ABC, abstractmethod
from typing import List, Dict

import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from songpop.data import *

log = logging.getLogger(__name__)


class Metric(ABC):
    @abstractmethod
    def compute_value(self, y_ground_truth: np.ndarray, y_predicted: np.ndarray) -> float:
        """
        :param y_ground_truth: the ground truth values
        :param y_predicted: the model's predictions
        :return: the metric value
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        :return: the name of the metric
        """
        pass

    @abstractmethod
    def is_larger_better(self) -> bool:
        """
        :return: True if the metric is a quality metric where larger is better,
            False if it is an error metric where lower is better
        """
        pass


class MetricMeanAbsError(Metric):
    def compute_value(self, y_ground_truth: np.ndarray, y_predicted: np.ndarray) -> float:
        return metrics.mean_absolute_error(y_ground_truth, y_predicted)

    def get_name(self) -> str:
        return "MAE"

    def is_larger_better(self) -> bool:
        return False


class MetricR2(Metric):
    def compute_value(self, y_ground_truth: np.ndarray, y_predicted: np.ndarray) -> float:
        return metrics.r2_score(y_ground_truth, y_predicted)

    def get_name(self) -> str:
        return "R²"

    def is_larger_better(self) -> bool:
        return True


class MetricRelFreqErrorWithin(Metric):
    def __init__(self, max_error: float):
        self.max_error = max_error

    def compute_value(self, y_ground_truth: np.ndarray, y_predicted: np.ndarray) -> float:
        cnt = 0
        for y1, y2 in zip(y_ground_truth, y_predicted):
            if abs(y1 - y2) <= self.max_error:
                cnt += 1
        return cnt / len(y_ground_truth)

    def get_name(self) -> str:
        return f"RelFreqErrWithin[{self.max_error}]"

    def is_larger_better(self) -> bool:
        return True


class ModelEvaluation:
    """
    Supports the evaluation of regression models, collecting the results.
    """
    def __init__(self, X: pd.DataFrame, y: pd.Series,
            metrics: List[Metric],
            test_size: float = 0.3, shuffle: bool = True, random_state: int = 42):
        """
        :param X: the inputs
        :param y: the prediction targets
        :param metrics: the metrics to consider in the evaluation; the first metric shall be the relevant one,
            by which results shall be sorted (best first)
        :param test_size: the fraction of the data to reserve for testing
        :param shuffle: whether to shuffle the data prior to splitting
        :param random_state: the random seed to use for shuffling
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y,
            random_state=random_state, test_size=test_size, shuffle=shuffle)
        self.metrics = metrics
        self.result_rows = []

    def evaluate_model(self, model) -> Dict[str, float]:
        """
        Fits and evaluates the given model, collecting the evaluation results.

        :param model: the model to evaluate
        :return: a dictionary containing all metric values
        """
        log.info(f"Fitting {model}")
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        metrics_dict = {}
        for metric in self.metrics:
            metric_value = metric.compute_value(self.y_test, y_pred)
            metrics_dict[metric.get_name()] = metric_value
            log.info(f"{model}: {metric.get_name()}={metric_value:.3f}")
        self.result_rows.append({"model": str(model), **metrics_dict})
        return metrics_dict

    class Result:
        def __init__(self, df: pd.DataFrame, metric: Metric):
            """
            :param df: a data frame containing model names (column 'model') and metrics (other columns)
            :param metric: the metric by which the data frame is to be sorted (best model first)
            """
            self.df = df.sort_values(metric.get_name(), ascending=not metric.is_larger_better())
            self.metric = metric

        def get_best_model_name(self) -> str:
            return self.df["model"].iloc[0]

        def get_best_metric_value(self) -> float:
            return self.df[self.metric.get_name()].iloc[0]

    def get_result(self) -> Result:
        """
        :return: an object containing evaluation results
        """
        df = pd.DataFrame(self.result_rows)
        return self.Result(df, self.metrics[0])


def main():
    dataset = Dataset(10000)
    X, y = dataset.load_xy_projected_scaled()

    # evaluate models
    ev = ModelEvaluation(X, y, [MetricR2(), MetricMeanAbsError(), MetricRelFreqErrorWithin(10)])
    ev.evaluate_model(LogisticRegression(solver='lbfgs', max_iter=1000))
    ev.evaluate_model(KNeighborsRegressor(n_neighbors=1))
    ev.evaluate_model(RandomForestRegressor(n_estimators=100))
    ev.evaluate_model(DecisionTreeRegressor(random_state=42, max_depth=2))
    result = ev.get_result()
    log.info(f"Results:\n{result.df.to_string()}")
    log.info(f"Best model is '{result.get_best_model_name()}' with {result.metric.get_name()}={result.get_best_metric_value()}'")


if __name__ == '__main__':
    logging.run_main(main)