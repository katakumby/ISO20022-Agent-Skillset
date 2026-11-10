---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.1 Equity <Eqty>", "28.4.2.2.1.1.1 PreferenceToIncome <PrefToIncm>"]
file_pages: [1587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.1.1 PreferenceToIncome <PrefToIncm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1587 to 1587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1587

```text
Equity <Eqty> contains the following Equity3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreferenceToIncome <PrefToIncm> [1..1]  1587
{Or     Code <Cd> [1..1] CodeSet 1587
Or}     Proprietary <Prtry> [1..1] ± 1587
   MaturityDate <MtrtyDt> [0..1] DateTime 1588
   NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 1588
   ParValue <ParVal> [0..1] Amount C1, C5 1588
   VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 1589
28.4.2.2.1.1.1  PreferenceToIncome <PrefToIncm>
Presence: [1..1]
Definition: Indicates the level of priority to claim on income and assets of the company in case of the
payment of dividends and in the event of a bankruptcy, for example, ordinary/common stocks, preferred
stocks, subordinated debt, etc.
PreferenceToIncome <PrefToIncm> contains one of the following PreferenceToIncome5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1587
Or}   Proprietary <Prtry> [1..1] ± 1587
28.4.2.2.1.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Preference to income expressed as an ISO 20022 code.
Datatype: "PreferenceToIncome1Code" on page 3280
CodeName Name Definition
ORDN Ordinary Indicates an ordinary/common
preference to income.
PFRD Preferred Indicates a preferred claim upon income
and assets.
28.4.2.2.1.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Preference to income expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1587 August 2026
```

