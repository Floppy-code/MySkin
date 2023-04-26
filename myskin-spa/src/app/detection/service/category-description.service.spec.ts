import { TestBed } from '@angular/core/testing';

import { CategoryDescriptionService } from './category-description.service';

describe('CategoryDescriptionService', () => {
  let service: CategoryDescriptionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CategoryDescriptionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
