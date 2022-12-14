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
  private predictionResults?: Observable<PredictionResult>;

  constructor(private predictionService: PredictionService) {}

  //TODO
  predictFromImage(image: ImageBitmap): void {
    return;
  }
}
