---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>", "2.4.2.15.17.2 POI <POI>", "2.4.2.15.17.2.5 Component <Cmpnt>", "2.4.2.15.17.2.5.5 SerialNumber <SrlNb>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17.2.5.5 SerialNumber <SrlNb>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
Datatype: "Max16Text" on page 915
2.4.2.15.17.2.5.5  SerialNumber <SrlNb>
Presence: [0..1]
Definition: Serial number of a component.
Datatype: "Max35Text" on page 916
2.4.2.15.17.2.5.6  ApprovalNumber <ApprvlNb>
Presence: [0..*]
Definition: Unique approval number for a component, delivered by a certification body.
Usage: More than one approval number could be present, when assigned by different bodies. The
certification body identification must be provided within the approval number (for example at the
beginning of the value).
Datatype: "Max70Text" on page 917
2.4.2.15.17.3  AggregatedEntry <AggtdNtry>
Presence: [0..1]
Definition: Card entry details, based on card transaction aggregated data performed by the account
servicer.
AggregatedEntry <AggtdNtry> contains the following CardAggregated2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalService <AddtlSvc> [0..1] CodeSet 92
   TransactionCategory <TxCtgy> [0..1] CodeSet 93
   SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 93
   SequenceNumberRange <SeqNbRg> [0..1]  93
     FirstTransaction <FrstTx> [0..1] Text 93
     LastTransaction <LastTx> [0..1] Text 93
   TransactionDateRange <TxDtRg> [0..1] ± 94
2.4.2.15.17.3.1  AdditionalService <AddtlSvc>
Presence: [0..1]
Definition: Service in addition to the main service.
Datatype: "CardPaymentServiceType2Code" on page 890
CodeName Name Definition
AGGR Aggregation Aggregation of low payments.
DCCV DCC Dynamic currency conversion (DCC).
GRTT Gratuity Card payment with gratuity.
INSP Instalment Instalment payment.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
92 March 2026
```

