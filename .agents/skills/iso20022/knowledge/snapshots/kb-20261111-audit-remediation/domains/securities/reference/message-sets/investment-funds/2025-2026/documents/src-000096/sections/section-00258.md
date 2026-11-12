---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.26 ValueForMoney <ValForMny>", "15.4.5.26.5 OtherReviewRelatedToValueAndOrChargesUK <OthrRvwRltdToValAndOrChrgsUK>"]
file_pages: [363, 364]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.26.5 OtherReviewRelatedToValueAndOrChargesUK <OthrRvwRltdToValAndOrChrgsUK>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 363 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
CodeName Name Definition
PRI2 ChangesRequired Review indicates significant changes are
required in order to provide fair value.
PRI1 FairValue Product expected to provide fair value
for a reasonably foreseeable period.
15.4.5.26.5  OtherReviewRelatedToValueAndOrChargesUK
<OthrRvwRltdToValAndOrChrgsUK>
Presence: [0..1]
Definition: Specifies the outcome of other review about fair value and/or charges. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 09070.
Datatype: "OtherReviewRelatedToValueAndOrChargesUKType1Code" on page 5335
CodeName Name Definition
REVA ESMA In line with the ESMA supervisory
briefing on the supervision of costs in
UCITS and AIFs or relevant NCA
supervisory activity.
REVO Other In line with other local requirements or
procedures.
15.4.5.26.6  FurtherInformationUK <FrthrInfUK>
Presence: [0..1]
Definition: Link to sources of relevant information. When used in reference to MiFID, this is in the scope
of the European MiFID Template (EMT) reference 09080.
Datatype: "Max350Text" on page 5403
15.4.5.26.7  ReviewDateUK <RvwDtUK>
Presence: [0..1]
Definition: Specifies the date of the value assessment review, date of the COLL assessment of the
published value report, or initial launch date. The initial launch date must be used if the initial
assessment has not yet become subject to review or where the first COLL assessment of value report
has yet to be published. When used in reference to MiFID, this is in the scope of the European MiFID
Template (EMT) reference 09090.
Datatype: "ISODate" on page 5388
15.4.5.26.8  ReviewNextDueUK <RvwNxtDueUK>
Presence: [0..1]
Definition: Specifies the date of next assessment review. Empty if the initial assessment is not expected
to require a review. For example, 'bid-only' products. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 09100.
Datatype: "ISODate" on page 5388
15.4.5.27  Extension <Xtnsn>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 363 May 2026
```

## File page 364

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C17 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 364 May 2026
```

