---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.1 Identification <Id>"]
file_pages: [929]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 929 to 929.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 929

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IncomeCurrentPeriod <IncmCurPrd> [0..1] Amount C1 935
     IncomeLimitNextPeriod <IncmLmtNxtPrd> [0..1] Amount C1 936
     AdditionalInformation <AddtlInf> [0..*] ± 936
   FlexibleDrawdownTriggeredDate
<FlxblDrwdwnTrggrdDt>
[0..1] Date 936
   TrancheDate <TrchDt> [0..1] Date 936
   AdditionalInformation <AddtlInf> [0..*] ± 937
Constraints
• BeneficiaryDetailsRule
If RecipientOfDrawdownIndicator is "false" or "0" (No), then BeneficiaryDetails is not allowed.
If RecipientOfDrawdownIndicator is "true" or "1" (Yes), then BeneficiaryDetails may be present.
On Condition
    /RecipientOfDrawdownIndicator is equal to value 'false'
 Or    /RecipientOfDrawdownIndicator is equal to value '0'
Following Must be True
    /BeneficiaryDetails Must be absent
34.4.4.21.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the drawdown.
Datatype: "Max140Text" on page 5402
34.4.4.21.2  TrancheType <TrchTp>
Presence: [1..1]
Definition: Type of drawdown tranche.
TrancheType <TrchTp> contains one of the following elements (see "DrawdownType2Choice" on
page 4791 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4791
Or}   Proprietary <Prtry> [1..1] ± 4791
34.4.4.21.3  ApplicableRules <AplblRules>
Presence: [0..1]
Definition: Specifies the rules that are applicable to the drawdown. For example, in the UK market, the
pre-A-day rule that was introduced on 6 April 2006.)
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 929 May 2026
```

