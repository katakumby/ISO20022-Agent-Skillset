---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.1 Card <Card>", "4.4.2.14.17.1.1 PlainCardData <PlainCardData>", "4.4.2.14.17.1.1.1 PAN <PAN>"]
file_pages: [602]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.1.1.1 PAN <PAN>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 602 to 602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 602

```text
PlainCardData <PlainCardData> contains the following PlainCardData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
4.4.2.14.17.1.1.1  PAN <PAN>
Presence: [1..1]
Definition: Primary Account Number (PAN) of the card, or card number.
Datatype: "Min8Max28NumericText" on page 918
4.4.2.14.17.1.1.2  CardSequenceNumber <CardSeqNb>
Presence: [0..1]
Definition: Identify a card inside a set of cards with the same card number (PAN).
Datatype: "Min2Max3NumericText" on page 917
4.4.2.14.17.1.1.3  EffectiveDate <FctvDt>
Presence: [0..1]
Definition: Date as from which the card can be used.
Datatype: "ISOYearMonth" on page 919
4.4.2.14.17.1.1.4  ExpiryDate <XpryDt>
Presence: [1..1]
Definition: Expiry date of the card.
Datatype: "ISOYearMonth" on page 919
4.4.2.14.17.1.1.5  ServiceCode <SvcCd>
Presence: [0..1]
Definition: Services attached to the card, as defined in ISO 7813.
Datatype: "Exact3NumericText" on page 913
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
602 March 2026
```

