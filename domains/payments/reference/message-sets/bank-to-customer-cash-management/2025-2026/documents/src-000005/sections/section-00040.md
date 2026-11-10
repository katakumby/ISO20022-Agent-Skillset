---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>", "2.4.2.15.17.1 Card <Card>", "2.4.2.15.17.1.1 PlainCardData <PlainCardData>", "2.4.2.15.17.1.1.1 PAN <PAN>"]
file_pages: [84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17.1.1.1 PAN <PAN>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 84 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
PlainCardData <PlainCardData> contains the following PlainCardData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
2.4.2.15.17.1.1.1  PAN <PAN>
Presence: [1..1]
Definition: Primary Account Number (PAN) of the card, or card number.
Datatype: "Min8Max28NumericText" on page 918
2.4.2.15.17.1.1.2  CardSequenceNumber <CardSeqNb>
Presence: [0..1]
Definition: Identify a card inside a set of cards with the same card number (PAN).
Datatype: "Min2Max3NumericText" on page 917
2.4.2.15.17.1.1.3  EffectiveDate <FctvDt>
Presence: [0..1]
Definition: Date as from which the card can be used.
Datatype: "ISOYearMonth" on page 919
2.4.2.15.17.1.1.4  ExpiryDate <XpryDt>
Presence: [1..1]
Definition: Expiry date of the card.
Datatype: "ISOYearMonth" on page 919
2.4.2.15.17.1.1.5  ServiceCode <SvcCd>
Presence: [0..1]
Definition: Services attached to the card, as defined in ISO 7813.
Datatype: "Exact3NumericText" on page 913
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
84 March 2026
```

