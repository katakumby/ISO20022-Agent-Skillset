---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.1 Card <Card>", "4.4.2.14.18.2.26.1.1 PlainCardData <PlainCardData>", "4.4.2.14.18.2.26.1.1.1 PAN <PAN>"]
file_pages: [756]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.1.1.1 PAN <PAN>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 756 to 756.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 756

```text
PlainCardData <PlainCardData> contains the following PlainCardData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
4.4.2.14.18.2.26.1.1.1  PAN <PAN>
Presence: [1..1]
Definition: Primary Account Number (PAN) of the card, or card number.
Datatype: "Min8Max28NumericText" on page 918
4.4.2.14.18.2.26.1.1.2  CardSequenceNumber <CardSeqNb>
Presence: [0..1]
Definition: Identify a card inside a set of cards with the same card number (PAN).
Datatype: "Min2Max3NumericText" on page 917
4.4.2.14.18.2.26.1.1.3  EffectiveDate <FctvDt>
Presence: [0..1]
Definition: Date as from which the card can be used.
Datatype: "ISOYearMonth" on page 919
4.4.2.14.18.2.26.1.1.4  ExpiryDate <XpryDt>
Presence: [1..1]
Definition: Expiry date of the card.
Datatype: "ISOYearMonth" on page 919
4.4.2.14.18.2.26.1.1.5  ServiceCode <SvcCd>
Presence: [0..1]
Definition: Services attached to the card, as defined in ISO 7813.
Datatype: "Exact3NumericText" on page 913
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
756 March 2026
```

