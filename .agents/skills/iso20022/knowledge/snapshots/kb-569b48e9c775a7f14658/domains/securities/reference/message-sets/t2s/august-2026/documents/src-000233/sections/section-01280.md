---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.1 Equity <Eqty>", "32.4.3.1.1.2.1.1 PreferenceToIncome <PrefToIncm>"]
file_pages: [1865]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.1.1 PreferenceToIncome <PrefToIncm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1865 to 1865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1865

```text
Equity <Eqty> contains the following Equity3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreferenceToIncome <PrefToIncm> [1..1]  1865
{Or     Code <Cd> [1..1] CodeSet 1865
Or}     Proprietary <Prtry> [1..1] ± 1865
   MaturityDate <MtrtyDt> [0..1] DateTime 1866
   NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1866
   ParValue <ParVal> [0..1] Amount C1, C5 1866
   VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1867
32.4.3.1.1.2.1.1  PreferenceToIncome <PrefToIncm>
Presence: [1..1]
Definition: Indicates the level of priority to claim on income and assets of the company in case of the
payment of dividends and in the event of a bankruptcy, for example, ordinary/common stocks, preferred
stocks, subordinated debt, etc.
PreferenceToIncome <PrefToIncm> contains one of the following PreferenceToIncome5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1865
Or}   Proprietary <Prtry> [1..1] ± 1865
32.4.3.1.1.2.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Preference to income expressed as an ISO 20022 code.
Datatype: "PreferenceToIncome1Code" on page 3280
CodeName Name Definition
ORDN Ordinary Indicates an ordinary/common
preference to income.
PFRD Preferred Indicates a preferred claim upon income
and assets.
32.4.3.1.1.2.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Preference to income expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1865 August 2026
```

