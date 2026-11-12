---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.8 Market", "22.1.8.3 TradingVenueAttributes2", "22.1.8.3.4 RequestForAdmissionDate <ReqForAdmssnDt>"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.8.3.4 RequestForAdmissionDate <ReqForAdmssnDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
Definition: Date and time the issuer has approved the admission to trading or trading of its financial
instruments on the trading venue.
Datatype: "ISODateTime" on page 449
22.1.8.3.4  RequestForAdmissionDate <ReqForAdmssnDt>
Presence: [0..1]
Definition: Date and time when the request for admission on the trading venue was made for the
instrument.
Datatype: "ISODateTime" on page 449
22.1.8.3.5  FirstTradeDate <FrstTradDt>
Presence: [0..1]
Definition: Date and time of the admission to trading on the trading venue or the date and time when the
instrument was first traded or an order or quote was first received by the trading venue.
Datatype: "ISODateTime" on page 449
22.1.8.3.6  TerminationDate <TermntnDt>
Presence: [0..1]
Definition: Date and time when the financial instrument ceases to be traded or to be admitted to trading
on the trading venue. Where this date and time is unavailable, the field shall not be populated.
Datatype: "ISODateTime" on page 449
22.1.8.4  TradingVenueIdentification1Choice
Definition: Trade venue related fields.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentificationCode <MktIdCd> [1..1] IdentifierSet 337
Or   NationalCompetentAuthority <NtlCmptntAuthrty> [1..1] CodeSet C4 337
Or}   Other <Othr> [1..1] ± 338
Constraints
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
22.1.8.4.1  MarketIdentificationCode <MktIdCd>
Presence: [1..1]
Definition: Identification used where reporting entity uses a market identification code (MIC).
Datatype: "MICIdentifier" on page 451
22.1.8.4.2  NationalCompetentAuthority <NtlCmptntAuthrty>
Presence: [1..1]
Definition: Identification used where reporting entity is a national competent authority.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
337 July 2025
```

