---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.42 CorporateActionEventType73Choice", "7.1.18.42.2 Proprietary <Prtry>"]
file_pages: [410]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.42.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 410 to 410.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 410

```text
CodeName Name Definition
WRTH Worthless Booking out of valueless securities.
ACCU Accumulation Funds related event in which the income
(for example accumulation units) that
accrues during an accounting period is
retained within the fund instead of being
paid away to investors. The retained
income is nonetheless deemed to have
been distributed to investors for tax
purposes.
MTNG SecuritiesHoldersMeeting Ordinary or annual or extraordinary or
special general meeting.
INFO Information Information provided by the issuer
having no accounting/financial impact on
the holder.
TNDP TaxOnNonDistributedProceeds Taxable component on non-distributed
proceeds, for example, Australian
deemed income or US 871m income
regulation.
7.1.18.42.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Corporate action event type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.43  Statement89
Definition: Defines the criteria used to report on the securities account positions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOrPeriod <DtOrPrd> [0..1] ± 410
   HistoricData <HstrcData> [1..1] Indicator 411
   StatementType <StmtTp> [0..1] ± 411
7.1.18.43.1  DateOrPeriod <DtOrPrd>
Presence: [0..1]
Definition: Date or period of the statement.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 410 March 2026
```

