---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>", "2.4.2.15.17.1 Card <Card>", "2.4.2.15.17.1.1 PlainCardData <PlainCardData>"]
file_pages: [83]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17.1.1 PlainCardData <PlainCardData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 83 to 83.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
Card <Card> contains the following PaymentCard4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlainCardData <PlainCardData> [0..1]  83
     PAN <PAN> [1..1] Text 84
     CardSequenceNumber <CardSeqNb> [0..1] Text 84
     EffectiveDate <FctvDt> [0..1] YearMonth 84
     ExpiryDate <XpryDt> [1..1] YearMonth 84
     ServiceCode <SvcCd> [0..1] Text 84
     TrackData <TrckData> [0..*]  85
       TrackNumber <TrckNb> [0..1] Text 85
       TrackValue <TrckVal> [1..1] Text 85
     CardSecurityCode <CardSctyCd> [0..1]  85
       CSCManagement <CSCMgmt> [1..1] CodeSet 85
       CSCValue <CSCVal> [0..1] Text 86
   CardCountryCode <CardCtryCd> [0..1] Text 86
   CardBrand <CardBrnd> [0..1] ± 86
   AdditionalCardData <AddtlCardData> [0..1] Text 86
2.4.2.15.17.1.1  PlainCardData <PlainCardData>
Presence: [0..1]
Definition: Sensitive data associated with the card performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
83 March 2026
```

