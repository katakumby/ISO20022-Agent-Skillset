---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.1 Card <Card>", "4.4.2.14.18.2.26.1.1 PlainCardData <PlainCardData>"]
file_pages: [755]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.1.1 PlainCardData <PlainCardData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 755 to 755.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 755

```text
Card <Card> contains the following PaymentCard4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlainCardData <PlainCardData> [0..1]  755
     PAN <PAN> [1..1] Text 756
     CardSequenceNumber <CardSeqNb> [0..1] Text 756
     EffectiveDate <FctvDt> [0..1] YearMonth 756
     ExpiryDate <XpryDt> [1..1] YearMonth 756
     ServiceCode <SvcCd> [0..1] Text 756
     TrackData <TrckData> [0..*]  757
       TrackNumber <TrckNb> [0..1] Text 757
       TrackValue <TrckVal> [1..1] Text 757
     CardSecurityCode <CardSctyCd> [0..1]  757
       CSCManagement <CSCMgmt> [1..1] CodeSet 757
       CSCValue <CSCVal> [0..1] Text 758
   CardCountryCode <CardCtryCd> [0..1] Text 758
   CardBrand <CardBrnd> [0..1] ± 758
   AdditionalCardData <AddtlCardData> [0..1] Text 758
4.4.2.14.18.2.26.1.1  PlainCardData <PlainCardData>
Presence: [0..1]
Definition: Sensitive data associated with the card performing the transaction.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
755 March 2026
```

