---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.27 OrderWaiver1", "66.1.26.27.1 OrderWaiverReason <OrdrWvrRsn>", "66.1.26.27.1.2 Proprietary <Prtry>"]
file_pages: [4783]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.27.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4783 to 4783.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4783

```text
CodeName Name Definition
BMIN BelowMinimumInvestmentAmount Amount of subscription is below the
minimum initial investment amount.
CUTO CutOffDate Cut off date has been passed.
COMW CommissionWaiver Standard commission is waived.
66.1.26.27.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the waiver expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.26.27.2  InformationValue <InfVal>
Presence: [0..1]
Definition: Additional information about the order waiver.
Datatype: "Max350Text" on page 5403
66.1.26.28  MainFundOrderDeskLocation1
Definition: U-003-2009 Addition and Modification of choice component. S-009-2009 They are not valid
business options in the redemption processing context. S-015-2009 Add new data elements to indicate
time zone.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 4783
   TimeZoneOffSet <TmZoneOffSet> [1..1]  4784
     Sign <Sgn> [1..1] Indicator 4784
     NumberOfHours <NbOfHrs> [1..1] Time 4784
66.1.26.28.1  Country <Ctry>
Presence: [1..1]
Definition: Country in which it is authorised to commercialise the fund.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4783 May 2026
```

