---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.6 TaxRemittance <TaxRmt>", "3.4.3.7.12.11.2.6.11 Record <Rcrd>", "3.4.3.7.12.11.2.6.11.7 Period <Prd>", "3.4.3.7.12.11.2.6.11.7.3 FromToDate <FrToDt>"]
file_pages: [246]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.6.11.7.3 FromToDate <FrToDt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 246 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
CodeName Name Definition
MM02 SecondMonth Tax is related to the first month of the
period.
MM03 ThirdMonth Tax is related to the third month of the
period.
MM04 FourthMonth Tax is related to the fourth month of the
period.
MM05 FifthMonth Tax is related to the fifth month of the
period.
MM06 SixthMonth Tax is related to the sixth month of the
period.
MM07 SeventhMonth Tax is related to the seventh month of
the period.
MM08 EighthMonth Tax is related to the eighth month of the
period.
MM09 NinthMonth Tax is related to the ninth month of the
period.
MM10 TenthMonth Tax is related to the tenth month of the
period.
MM11 EleventhMonth Tax is related to the eleventh month of
the period.
MM12 TwelfthMonth Tax is related to the twelfth month of the
period.
QTR1 FirstQuarter Tax is related to the first quarter of the
period.
QTR2 SecondQuarter Tax is related to the second quarter of
the period.
QTR3 ThirdQuarter Tax is related to the third quarter of the
period.
QTR4 FourthQuarter Tax is related to the forth quarter of the
period.
HLF1 FirstHalf Tax is related to the first half of the
period.
HLF2 SecondHalf Tax is related to the second half of the
period.
3.4.3.7.12.11.2.6.11.7.3  FromToDate <FrToDt>
Presence: [0..1]
Definition: Range of time between a start date and an end date for which the tax report is provided.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 534 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 534
   ToDate <ToDt> [1..1] Date 534
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 246 March 2026
```

