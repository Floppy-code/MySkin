import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PageNotFoundComponent } from './core/component/page-not-found/page-not-found.component';
import { WelcomeComponent } from './core/component/welcome/welcome.component';

const routes: Routes = [
  { path: '', component: WelcomeComponent},
  { path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
