import { Component, Input } from '@angular/core';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { CategoryDescriptionService } from '../../service/category-description.service';

@Component({
  selector: 'app-detection-results',
  templateUrl: './detection-results.component.html',
  styleUrls: ['./detection-results.component.scss'],
})
export class DetectionResultsComponent {
  @Input() PredictionResult?: PredictionResult;

  displayedColumns: string[] = ['label-id', 'label-name', 'label-probability'];

  constructor(public descriptionService: CategoryDescriptionService) {}

  public GetCategoryDescription(): string {
    var category =
      this.PredictionResult?.prediction_probabilities[0].label_name;
    return this.descriptionService.GetCategoryDescription(category!);
  }
}
