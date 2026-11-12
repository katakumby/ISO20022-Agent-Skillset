---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.1 PlaceOfListing <PlcOfListg>"]
file_pages: [67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.1 PlaceOfListing <PlcOfListg>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 67 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 67

```text
3.4.6.1  PlaceOfListing <PlcOfListg>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
PlaceOfListing <PlcOfListg> contains one of the following elements (see
"MarketIdentification3Choice" on page 283 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 284
Or}   Description <Desc> [1..1] Text 284
3.4.6.2  Rating <Ratg>
Presence: [0..1]
Definition: Assessment of securities credit and investment risk.
Rating <Ratg> contains the following elements (see "Rating1" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RatingScheme <RatgSchme> [1..1] Text 518
   ValueDate <ValDt> [1..1] DateTime 518
   ValueIdentification <ValId> [1..1] IdentifierSet 518
3.4.6.3  CertificateNumber <CertNb>
Presence: [0..1]
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Datatype: "Max35Text" on page 669
3.4.6.4  DayCountBasis <DayCntBsis>
Presence: [0..1]
Definition: Specifies the computation method of (accrued) interest of the security.
DayCountBasis <DayCntBsis> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 370 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 371
Or}   Proprietary <Prtry> [1..1] ± 374
3.4.6.5  RegistrationForm <RegnForm>
Presence: [0..1]
Definition: Specifies the form, ie, ownership, of the security.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 67 February 2025
```

