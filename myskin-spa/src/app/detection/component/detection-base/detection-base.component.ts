import { formatDate } from '@angular/common';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { PredictionService } from '../../service/prediction.service';

@Component({
  selector: 'app-detection-base',
  templateUrl: './detection-base.component.html',
  styleUrls: ['./detection-base.component.scss'],
})
export class DetectionBaseComponent {
  public predictionResult$?: Observable<PredictionResult>;

  constructor(private predictionService: PredictionService) {
    this.predictionResult$ = this.predictionService.predictionResult$;
  }

  imageUploadedHandler(file: File): void {
    console.log('Received image from child component!');
    this.predictFromImage(file);
  }

  predictFromImage(file: File): void {
    console.log('Prediction initiated!');
    this.predictionService.predict(file);
  }
}
