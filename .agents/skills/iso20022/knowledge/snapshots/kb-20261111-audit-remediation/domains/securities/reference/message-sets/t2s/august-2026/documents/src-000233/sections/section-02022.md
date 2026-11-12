---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["80 semt.040.001.01 SecuritiesAccountPositionResponseV01", "80.4 Message Building Blocks"]
file_pages: [2753]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.040.001.01"]
---

# 80.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2753 to 2753.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2753

```text
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C31 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C32 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C33 SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
C34 SubAccountReportingRule
If ReportGeneralDetails/ActivityIndicator is TRUE (Yes) and ReportGeneralDetails/
SubAccountIndicator is TRUE (YES), then Balances/SubAccountDetails must be present and
Balances/BalanceForAccount must be absent.
This constraint is defined at the MessageDefinition level.
C35 SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
C36 SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
C37 SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
C38 SubSafekeepingReportingRule
Use of consolidated reports on a sub-safekeeping account must be bilaterally agreed between
sender and receiver.
C39 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C40 TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if
bilaterally agreed between the sender and receiver.
C41 ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
80.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.040.001.01
SecuritiesAccountPositionResponseV01
Target2-Securities 2753 August 2026
```

