import { PredictionResult } from './prediction-result';

export interface PredictionHistoryItem {
  prediction_date: string;
  prediction_result: PredictionResult;
}
