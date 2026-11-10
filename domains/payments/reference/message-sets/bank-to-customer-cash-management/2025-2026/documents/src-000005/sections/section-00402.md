---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.1 Card <Card>", "4.4.2.14.17.1.1 PlainCardData <PlainCardData>"]
file_pages: [601]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.1.1 PlainCardData <PlainCardData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 601 to 601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 601

```text
Card <Card> contains the following PaymentCard4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlainCardData <PlainCardData> [0..1]  601
     PAN <PAN> [1..1] Text 602
     CardSequenceNumber <CardSeqNb> [0..1] Text 602
     EffectiveDate <FctvDt> [0..1] YearMonth 602
     ExpiryDate <XpryDt> [1..1] YearMonth 602
     ServiceCode <SvcCd> [0..1] Text 602
     TrackData <TrckData> [0..*]  603
       TrackNumber <TrckNb> [0..1] Text 603
       TrackValue <TrckVal> [1..1] Text 603
     CardSecurityCode <CardSctyCd> [0..1]  603
       CSCManagement <CSCMgmt> [1..1] CodeSet 603
       CSCValue <CSCVal> [0..1] Text 604
   CardCountryCode <CardCtryCd> [0..1] Text 604
   CardBrand <CardBrnd> [0..1] ± 604
   AdditionalCardData <AddtlCardData> [0..1] Text 604
4.4.2.14.17.1.1  PlainCardData <PlainCardData>
Presence: [0..1]
Definition: Sensitive data associated with the card performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
601 March 2026
```

