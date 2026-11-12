---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.17 CardTransaction <CardTx>", "3.4.2.15.17.1 Card <Card>", "3.4.2.15.17.1.1 PlainCardData <PlainCardData>"]
file_pages: [343]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.17.1.1 PlainCardData <PlainCardData>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 343 to 343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 343

```text
Card <Card> contains the following PaymentCard4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlainCardData <PlainCardData> [0..1]  343
     PAN <PAN> [1..1] Text 344
     CardSequenceNumber <CardSeqNb> [0..1] Text 344
     EffectiveDate <FctvDt> [0..1] YearMonth 344
     ExpiryDate <XpryDt> [1..1] YearMonth 344
     ServiceCode <SvcCd> [0..1] Text 344
     TrackData <TrckData> [0..*]  345
       TrackNumber <TrckNb> [0..1] Text 345
       TrackValue <TrckVal> [1..1] Text 345
     CardSecurityCode <CardSctyCd> [0..1]  345
       CSCManagement <CSCMgmt> [1..1] CodeSet 345
       CSCValue <CSCVal> [0..1] Text 346
   CardCountryCode <CardCtryCd> [0..1] Text 346
   CardBrand <CardBrnd> [0..1] ± 346
   AdditionalCardData <AddtlCardData> [0..1] Text 346
3.4.2.15.17.1.1  PlainCardData <PlainCardData>
Presence: [0..1]
Definition: Sensitive data associated with the card performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
343 March 2026
```

