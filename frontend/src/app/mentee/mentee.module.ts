import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { MenteeService } from './shared/mentee.service';
import { MenteeListComponent } from './components/mentee-list.component';
import { MenteeListingPage } from './mentee-listing/mentee-listing.page';
import { MenteeDetailPage } from './mentee-detail/mentee-detail.page';
import { LoaderService } from '../shared/service/loader.service'
import { ToastService } from '../shared/service/toast.service';
import { AlertService } from '../shared/service/alert.service';

import { IonicModule } from '@ionic/angular';

import { MenteePage } from './mentee.page';

const routes: Routes = [
  {
    path: '',
    component: MenteePage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [MenteePage]
})
export class MenteePageModule {}
