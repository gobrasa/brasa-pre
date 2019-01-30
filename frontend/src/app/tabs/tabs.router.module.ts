import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { TabsPage } from './tabs.page';
import { MenteeDetailPage } from '../mentee/mentee-detail/mentee-detail.page';
import { MenteePage } from '../mentee/mentee/mentee.page';
import { MenteeListingPage } from '../mentee/mentee-listing/mentee-listing.page';
import { MentorDetailPage } from '../mentor/mentor-detail/mentor-detail.page';
import { MentorPage } from '../mentor/mentor/mentor.page';
import { MentorListingPage } from '../mentor/mentor-listing/mentor-listing.page';
import { MenteeTestPage } from '../mentee/mentee-test/mentee-test.page'
import { MenteeEssayPage } from '../mentee/mentee-essay/mentee-essay.page'
//import { ContactPage } from '../contact/contact.page';
//import { CardDeckPage } from '../card/card-deck/card-deck.page';

const routes: Routes = [
  {
    path: 'tabs',
    component: TabsPage,
    children: [
      {
        path: 'mentee',
        component: MenteePage
      },
      {
        path: 'mentor',
        component: MentorPage
      },
      {
        path: 'mentor/detail',
        component: MentorDetailPage
      },
      {
        path: 'mentor/listing',
        component: MentorListingPage
      },
      {
        path: 'informacoes',
        component: MenteeDetailPage
      },{
        path: 'mentee/detail',
        component: MenteeDetailPage
      },{
        path: 'mentee/listing',
        component: MenteeListingPage
      },{
        path: 'mentee/test',
        component: MenteeTestPage
      },{
        path: 'mentee/essay',
        component: MenteeEssayPage
      }
      /*
      {
        path: 'about',
        outlet: 'about',
        component: AboutPage
      },
      {
        path: 'contact',
        outlet: 'contact',
        component: ContactPage
      },
      {
        path: 'card',
        outlet: 'card',
        component: CardDeckPage
      },
      {
        path: 'card/:cardId',
        outlet: 'card',
        component: CardDetailPage
      },
      {
        path: '/mentee/1',
        outlet: 'card',
        component: CardDetailPage
      },
      {
        path: 'card/:cardDeckGroup/:cardDeck',
        outlet: 'card',
        component: CardListingPage
      }
      */
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TabsPageRoutingModule {}