from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from meiduo_admin.home import home_view
from meiduo_admin.user import user_view
from meiduo_admin.sku import sku_views
from meiduo_admin.spec import spec_views
from meiduo_admin.option import option_views
from rest_framework.routers import DefaultRouter
from meiduo_admin.spu import spu_views
from meiduo_admin.image import image_views
from meiduo_admin.order import order_views

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    url(r'^statistical/total_count/$', home_view.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', home_view.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$', home_view.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', home_view.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$', home_view.UserMonthIncrementView.as_view()),
    url(r'^statistical/goods_day_views/$', home_view.GoodCategoryDayView.as_view()),
    url(r'^users/$', user_view.UserView.as_view()),

    url(r'^skus/categories/$', sku_views.SKUCategoryView.as_view()),

    url(r'^goods/simple/$', sku_views.GoodSimpleView.as_view()),

    url(r'^goods/(?P<spu_id>\d+)/specs/$', sku_views.GoodSpecsView.as_view()),

    url(r'^goods/brands/simple/$', spu_views.GoodBrandSimpleView.as_view()),

    url(r'^goods/channel/categories/$', spu_views.GoodCategorySimpleView.as_view()),

    url(r'^goods/channel/categories/(?P<parent_id>\d+)/$', spu_views.GoodCategorySimpleTwoThreeView.as_view()),

    url(r'^goods/images/$', spu_views.GoodsImagesView.as_view()),

    url(r'^goods/specs/simple/$', option_views.SpecSimpleView.as_view()),

    url(r'^skus/simple/$', image_views.SKUSimpleView.as_view()),

    # url(r'^orders/(?P<pk>\d+)/status/$', order_views.OrderModelViewSet.as_view({"put": "status"})),
]

# orders
router = DefaultRouter()
router.register("orders", order_views.OrderModelViewSet, base_name="orders")
urlpatterns += router.urls

# skus/images
router = DefaultRouter()
router.register("skus/images", image_views.ImageModelViewSet, base_name="images")
urlpatterns += router.urls

# specs/options/
router = DefaultRouter()
router.register("specs/options", option_views.OptionModelViewSet, base_name="option")
urlpatterns += router.urls

# goods/specs/
router = DefaultRouter()
router.register("goods/specs", spec_views.SpecModelViewSet, base_name="spec")
urlpatterns += router.urls

# goods
router = DefaultRouter()
router.register("goods", spu_views.SPUModelViewSet, base_name="goods")
urlpatterns += router.urls

# skus
router = DefaultRouter()
router.register("skus", sku_views.SKUModelViewSet, base_name="skus")
urlpatterns += router.urls
