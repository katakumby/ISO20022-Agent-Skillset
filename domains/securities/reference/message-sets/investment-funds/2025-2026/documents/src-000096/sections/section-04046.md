---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.205 SettlementDate1Code"]
file_pages: [5362]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.205 SettlementDate1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5362 to 5362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5362

```text
CodeName Name Definition
GATM GatedMultipleNAV Redemption has been gated. Multiple
redemptions and multiple prices will be
required.
GAT1 GatedOneNAV Redemption has been gated, all
settlement will be done at the same
price.
UCPS UnitsCashPartiallySettled Units and cash are both partially settled.
UPST UnitsPartiallySettled Units are partially settled.
66.2.2.205  SettlementDate1Code
Definition: Indicates the date of settlement in coded form.
Type: CodeSet
CodeName Name Definition
ASAP AsSoonAsPossible Transfer is to be effected as soon as
possible.
ENDC AtEndOfContract Transfer is to be effected at the end of
the contract.
WHIF WhenAndIfIssued Settlement takes place when the
financial instrument is issued by the
issuer.
66.2.2.206  SettlementInstructionReason1Code
Definition: Specifies the type of transaction.
Type: CodeSet
CodeName Name Definition
CSHI AllCredits Settlement of all credit amounts.
ALLL AllCreditsAndDebits Settlement of all credit and debit
amounts.
CSHO AllDebits Settlement of all debit amounts.
CHAR Charges Settlement of charges.
DIVI Dividend Settlement of dividends.
INTE Interest Settlement of interest.
SAVP InvestmentSavingsPlan Settlement of investments to a savings
plan.
REDM Redemption Settlement of redemptions or redemption
legs of a switch transaction.
SAVE SavingsPlan Settlement of investments to a savings
plan and withdrawals from a savings
plan.
BUYI SecuritiesPurchase Settlement of securities purchases.
SELL SecuritiesSale Settlement of securities sales.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5362 May 2026
```

