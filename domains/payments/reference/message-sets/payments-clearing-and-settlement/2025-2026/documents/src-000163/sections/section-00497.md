---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.6 TaxRemittance <TaxRmt>", "5.4.3.21.11.2.6.11 Record <Rcrd>", "5.4.3.21.11.2.6.11.8 TaxAmount <TaxAmt>", "5.4.3.21.11.2.6.11.8.4 Details <Dtls>", "5.4.3.21.11.2.6.11.8.4.1 Period <Prd>", "5.4.3.21.11.2.6.11.8.4.1.2 Type <Tp>"]
file_pages: [679]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.6.11.8.4.1.2 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 679 to 679.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 679

```text
Datatype: "ISOYear" on page 1247
5.4.3.21.11.2.6.11.8.4.1.2  Type <Tp>
Presence: [0..1]
Definition: Identification of the period related to the tax payment.
Datatype: "TaxRecordPeriod1Code" on page 1238
CodeName Name Definition
MM01 FirstMonth Tax is related to the second month of the
period.
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
5.4.3.21.11.2.6.11.8.4.1.3  FromToDate <FrToDt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
679 March 2026
```

