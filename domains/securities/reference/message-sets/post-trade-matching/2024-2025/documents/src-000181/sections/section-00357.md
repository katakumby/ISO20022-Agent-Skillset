---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.11 TradingPartyCapacity4Choice", "7.1.20.11.2 Proprietary <Prtry>"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.11.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
CodeName Name Definition
TAGT TransferAgent Party appointed by the Fund
Management Company. It updates
records of investor accounts to reflect
the daily investor purchases,
redemptions, switches, transfers, and re-
registrations. It ensures the timely
settlement of transactions, and may
provide tax information to the investor
and/or to its intermediaries. It may
calculate, collect, and rebate
commissions. It prepares and distributes
confirmations reflecting transactions,
resulting in unit or cash account
movements to the investor or the
investor's intermediary. It responds to
inquiries concerning account status, and
processes the income distribution.
7.1.20.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trading capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.20.12  ConfirmationPartyDetails9
Definition: Parties used for acting parties that apply either to the whole message or to individual sides.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 422
   AlternateIdentification <AltrnId> [0..1] ± 423
   ProcessingIdentification <PrcgId> [0..1] Text 423
   AdditionalInformation <AddtlInf> [0..1] ± C1 423
   InvestorProtectionAssociationMembership
<InvstrPrtcnAssoctnMmbsh>
[0..1] Indicator 424
7.1.20.12.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution, eg,
Dun & Bradstreet Identification.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 422 February 2025
```

