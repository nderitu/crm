$(document).ready(function() {
    $('.delete-order-btn').on('click', function() {
        $('#deleteOrderModal').modal('show');

        const orderId = $(this).data('order-id');
        $('#deleteOrderForm').attr('action', $(this).attr('href'));
        $('#deleteOrderItemName').text($(this).attr('data-order-item-name'));
        $('#deleteOrderForm input[name="pk"]').val(orderId);
    });
});