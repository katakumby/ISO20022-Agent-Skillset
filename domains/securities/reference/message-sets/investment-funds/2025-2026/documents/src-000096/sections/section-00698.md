---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.22 OtherDrawdownInformation <OthrDrwdwnInf>", "34.4.4.22.1 EmploymentDetails <MplymntDtls>", "34.4.4.22.1.7 EndDate <EndDt>"]
file_pages: [940]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.22.1.7 EndDate <EndDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 940 to 940.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 940

```text
34.4.4.22.1.7  EndDate <EndDt>
Presence: [0..1]
Definition: End date of the employment period.
EndDate <EndDt> contains one of the following elements (see "DateFormat42Choice" on page 4467
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
34.4.4.22.1.8  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the employment.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
34.4.4.22.2  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the drawdown.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
34.4.4.23  QueryResponse <QryRspn>
Presence: [0..*]
Definition: Response information.
Datatype: "Max350Text" on page 5403
34.4.4.24  StatusInitiator <StsInitr>
Presence: [0..1]
Definition: Party that initiates the status.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 940 May 2026
```

