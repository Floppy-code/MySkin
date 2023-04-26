import { Component } from '@angular/core';
import { PredictionHistoryItem } from 'src/app/core/model/prediction-history-item';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { CategoryDescriptionService } from '../../service/category-description.service';
import { PredictionHistoryService } from '../../service/prediction-history.service';

@Component({
  selector: 'app-detection-history',
  templateUrl: './detection-history.component.html',
  styleUrls: ['./detection-history.component.scss'],
})
export class DetectionHistoryComponent {
  public predictionResults: PredictionHistoryItem[] = [];
  public displayedColumns: string[] = [
    'label-id',
    'label-name',
    'label-probability',
  ];

  constructor(
    private predictionHistoryService: PredictionHistoryService,
    private categoryDescriptionService: CategoryDescriptionService
  ) {
    this.predictionResults = this.UpdatePredictionResults();
  }

  public UpdatePredictionResults(): Array<PredictionHistoryItem> {
    var results: PredictionHistoryItem[] | null =
      this.predictionHistoryService.getPredictionResults();
    if (results == null) {
      results = [];
    }

    return results;
  }

  public GetCategoryDescription(category: string): string {
    return this.categoryDescriptionService.GetCategoryDescription(category!);
  }
}
