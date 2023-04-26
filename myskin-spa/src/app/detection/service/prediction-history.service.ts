import { Injectable } from '@angular/core';
import { PredictionHistoryItem } from 'src/app/core/model/prediction-history-item';
import { PredictionResult } from '../../core/model/prediction-result';

@Injectable({
  providedIn: 'root',
})
export class PredictionHistoryService {
  private HistoryLocalStorageKey: string = 'DETECTION_HISTORY';

  constructor() {}

  public addPredictionResult(predictionResult: PredictionResult): void {
    var results = this.getPredictionResults();
    if (results == null) {
      results = [];
    }

    var predictionHistoryItem: PredictionHistoryItem = {
      prediction_date: new Date().toLocaleString(),
      prediction_result: predictionResult,
    };
    results.push(predictionHistoryItem);
    let resultsJson = JSON.stringify(results);

    console.log(resultsJson);
    localStorage.setItem(this.HistoryLocalStorageKey, resultsJson);
  }

  public getPredictionResults(): PredictionHistoryItem[] | null {
    var resultsJson = localStorage.getItem(this.HistoryLocalStorageKey);
    if (resultsJson == null) {
      console.log('No detection history results to load from local storage.');
      return null;
    }

    var results: PredictionHistoryItem[] = JSON.parse(resultsJson);
    return results;
  }

  public clearPredictionResults(): void {
    localStorage.removeItem(this.HistoryLocalStorageKey);
  }
}
