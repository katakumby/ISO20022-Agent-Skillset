---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.1 FinancialInstrument97", "13.1.6.1.2 Warrant <Warrt>"]
file_pages: [238]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.1.2 Warrant <Warrt>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 238 to 238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
Equity <Eqty> contains the following elements (see "Equity3" on page 147 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreferenceToIncome <PrefToIncm> [1..1]  147
{Or     Code <Cd> [1..1] CodeSet 147
Or}     Proprietary <Prtry> [1..1] ± 148
   MaturityDate <MtrtyDt> [0..1] DateTime 148
   NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 148
   ParValue <ParVal> [0..1] Amount C1, C5 148
   VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 149
13.1.6.1.2  Warrant <Warrt>
Presence: [0..1]
Definition: Financial instrument that gives the holder the right to purchase shares or bonds at a given
price within a specified time.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 238 March 2024
```

