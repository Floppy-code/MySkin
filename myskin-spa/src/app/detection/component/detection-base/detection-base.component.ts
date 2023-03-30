import { Component } from '@angular/core';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { PredictionItem } from 'src/app/core/model/predition-item';
import { PredictionService } from '../../service/prediction.service';

@Component({
  selector: 'app-detection-base',
  templateUrl: './detection-base.component.html',
  styleUrls: ['./detection-base.component.scss'],
})
export class DetectionBaseComponent {
  public predictionResult: PredictionResult;

  constructor(private predictionService: PredictionService) {
    this.predictionResult = { prediction_probabilities: [] };
  }

  imageUploadedHandler(base64Image: string): void {
    this.predictionService
      .predict(base64Image)
      .subscribe((items: PredictionItem[]) => {
        this.predictionResult.prediction_probabilities.length = 0;
        items.forEach((item) => {
          this.predictionResult.prediction_probabilities.push(item);
        });
        this.predictionResult.prediction_probabilities.sort(
          (item1, item2) => item2.probability - item1.probability
        );
      });
    console.log(this.predictionResult);
  }
}
