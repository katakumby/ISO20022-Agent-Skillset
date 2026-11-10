---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.1 Card <Card>", "2.4.2.15.18.2.26.1.1 PlainCardData <PlainCardData>"]
file_pages: [237]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.1.1 PlainCardData <PlainCardData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 237 to 237.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 237

```text
Card <Card> contains the following PaymentCard4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlainCardData <PlainCardData> [0..1]  237
     PAN <PAN> [1..1] Text 238
     CardSequenceNumber <CardSeqNb> [0..1] Text 238
     EffectiveDate <FctvDt> [0..1] YearMonth 238
     ExpiryDate <XpryDt> [1..1] YearMonth 238
     ServiceCode <SvcCd> [0..1] Text 238
     TrackData <TrckData> [0..*]  239
       TrackNumber <TrckNb> [0..1] Text 239
       TrackValue <TrckVal> [1..1] Text 239
     CardSecurityCode <CardSctyCd> [0..1]  239
       CSCManagement <CSCMgmt> [1..1] CodeSet 239
       CSCValue <CSCVal> [0..1] Text 240
   CardCountryCode <CardCtryCd> [0..1] Text 240
   CardBrand <CardBrnd> [0..1] ± 240
   AdditionalCardData <AddtlCardData> [0..1] Text 240
2.4.2.15.18.2.26.1.1  PlainCardData <PlainCardData>
Presence: [0..1]
Definition: Sensitive data associated with the card performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
237 March 2026
```

