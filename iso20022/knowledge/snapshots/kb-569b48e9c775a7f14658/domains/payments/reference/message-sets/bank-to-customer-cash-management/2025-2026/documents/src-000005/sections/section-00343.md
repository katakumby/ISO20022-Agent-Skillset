---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.1 Card <Card>", "3.4.2.15.18.2.26.1.1 PlainCardData <PlainCardData>"]
file_pages: [497]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.1.1 PlainCardData <PlainCardData>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 497 to 497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 497

```text
Card <Card> contains the following PaymentCard4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlainCardData <PlainCardData> [0..1]  497
     PAN <PAN> [1..1] Text 498
     CardSequenceNumber <CardSeqNb> [0..1] Text 498
     EffectiveDate <FctvDt> [0..1] YearMonth 498
     ExpiryDate <XpryDt> [1..1] YearMonth 498
     ServiceCode <SvcCd> [0..1] Text 498
     TrackData <TrckData> [0..*]  499
       TrackNumber <TrckNb> [0..1] Text 499
       TrackValue <TrckVal> [1..1] Text 499
     CardSecurityCode <CardSctyCd> [0..1]  499
       CSCManagement <CSCMgmt> [1..1] CodeSet 499
       CSCValue <CSCVal> [0..1] Text 500
   CardCountryCode <CardCtryCd> [0..1] Text 500
   CardBrand <CardBrnd> [0..1] ± 500
   AdditionalCardData <AddtlCardData> [0..1] Text 500
3.4.2.15.18.2.26.1.1  PlainCardData <PlainCardData>
Presence: [0..1]
Definition: Sensitive data associated with the card performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
497 March 2026
```

