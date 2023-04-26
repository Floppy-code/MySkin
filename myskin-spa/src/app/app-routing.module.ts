import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminBaseComponent } from './admin/component/admin-base/admin-base.component';
import { PageNotFoundComponent } from './core/component/page-not-found/page-not-found.component';
import { WelcomeComponent } from './core/component/welcome/welcome.component';
import { DetectionBaseComponent } from './detection/component/detection-base/detection-base.component';
import { DetectionHistoryComponent } from './detection/component/detection-history/detection-history.component';

const routes: Routes = [
  { path: '', component: WelcomeComponent },
  { path: 'detection', component: DetectionBaseComponent },
  { path: 'history', component: DetectionHistoryComponent },
  { path: 'admin', component: AdminBaseComponent },
  { path: '**', component: PageNotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
