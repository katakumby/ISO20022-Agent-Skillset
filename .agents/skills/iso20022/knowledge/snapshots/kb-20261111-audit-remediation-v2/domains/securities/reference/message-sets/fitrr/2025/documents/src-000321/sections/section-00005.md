---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03", "2.4 Message Building Blocks"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.016.001.03"]
---

# 2.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C5 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C6 DescriptionUsageRule
Description must be used alone as the last resort.
C7 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C8 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C9 MultiplierRule
Price Multiplier must not be zero.
C10 NumberRule
If Number is negative, then Sign must be present.
C11 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C12 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C13 SwapInOrSwapOutRule
SwapIn or SwapOut must be present or both.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 Transaction <Tx>
Presence: [1..*]
Definition: Provides the details of the reported securities transactions.
Approved by the Securities SEG on 17 July 2025 auth.016.001.03
FinancialInstrumentReportingTransactionReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
9 July 2025
```

