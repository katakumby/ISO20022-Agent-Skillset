---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.20 Tax <Tax>", "4.4.2.14.18.2.20.11 Record <Rcrd>", "4.4.2.14.18.2.20.11.8 TaxAmount <TaxAmt>", "4.4.2.14.18.2.20.11.8.4 Details <Dtls>", "4.4.2.14.18.2.20.11.8.4.1 Period <Prd>", "4.4.2.14.18.2.20.11.8.4.1.2 Type <Tp>"]
file_pages: [741]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.20.11.8.4.1.2 Type <Tp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 741 to 741.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 741

```text
Datatype: "ISOYear" on page 919
4.4.2.14.18.2.20.11.8.4.1.2  Type <Tp>
Presence: [0..1]
Definition: Identification of the period related to the tax payment.
Datatype: "TaxRecordPeriod1Code" on page 905
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
4.4.2.14.18.2.20.11.8.4.1.3  FromToDate <FrToDt>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
741 March 2026
```

