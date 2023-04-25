import { Component } from '@angular/core';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { PredictionItem } from 'src/app/core/model/predition-item';
import { PredictionHistoryService } from '../../service/prediction-history.service';
import { PredictionService } from '../../service/prediction.service';

@Component({
  selector: 'app-detection-base',
  templateUrl: './detection-base.component.html',
  styleUrls: ['./detection-base.component.scss'],
})
export class DetectionBaseComponent {
  public predictionResult: PredictionResult;

  constructor(
    private predictionService: PredictionService,
    private predictionHistoryService: PredictionHistoryService
  ) {
    this.predictionResult = { prediction_probabilities: [] };
  }

  imageUploadedHandler(base64Image: string): void {
    this.predictionService
      .predict(base64Image)
      .subscribe((items: PredictionItem[]) => {
        this.predictionResult.prediction_probabilities.length = 0;
        this.predictionResult.prediction_probabilities = items;
        this.predictionResult.prediction_probabilities.sort(
          (item1, item2) => item2.probability - item1.probability
        );
        this.predictionResult.prediction_probabilities.forEach(
          (item) => (item.probability = Math.round(item.probability * 100))
        );
        this.predictionHistoryService.addPredictionResult(
          this.predictionResult
        );
      });
    console.log(this.predictionResult);
  }
}
