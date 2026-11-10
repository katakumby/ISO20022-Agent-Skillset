---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Transparency Of Holdings", "SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1"]
content_origin: "source-transcription"
---

# SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Transparency Of Holdings / SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5903** SecuritiesBalanceTransparencyReport semt.041.001.02 Message 1

**P5904** Message 1 from the above diagram

**P5905** Description

**P5906** CUSC (CUSCLULL) sends a SecuritiesBalanceTransparencyReport message to ICSD (ICSDLULL) with a breakdown of the account that ICSD services for CUSC, account CUSC3333. (In the message, this account specified at the safekeeping account level.)

**P5907** For this account, CUSC specifies the holdings of two accounts of its clients.

**P5908** CUSC’s two clients account and holdings 

**P5909** [1.1]	Client CCXX (CCXXLULL), account CCXX-c1. For ISIN LU1234567890, the aggregated settled balance is 1500 units, the aggregated traded balance is 1700 units. (In the message, this is specified at account sub level 1 repetition 1.)

**P5910** The following balance breakdowns are specified:

**P5911** 150 units are traded and pending settlement (PNET).

**P5912** 50 units are traded and pending settlement is overdue (OPNT).

**P5913** [1.2]	Client CCYY (CCYYLULL), account CCYY-c2. For ISIN LU1234567890, the aggregated settled balance is 4700 units, the aggregated traded balance is 5000 units. (In the message, this is specified at account sub level 1 repetition 2.)

**P5914** The following balance breakdowns are specified:

**P5915** 260 units are traded and pending settlement (PNET).

**P5916** 40 units are traded and pending settlement is overdue (OPNT).

[T64 - complete table](../tables/tbl-0064.md)

**P5918** The other messages in this scenario are not illustrated with XML message instances.

**P5919**   


