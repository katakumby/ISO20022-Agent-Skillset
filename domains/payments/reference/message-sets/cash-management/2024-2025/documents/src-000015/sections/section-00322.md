---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["11 camt.012.001.08 DeleteLimitV08", "11.4 Message Building Blocks", "11.4.2 LimitDetails <LmtDtls>", "11.4.2.2 AllCurrentLimits <AllCurLmts>", "11.4.2.2.2 Type <Tp>", "11.4.2.2.2.2 Proprietary <Prtry>"]
file_pages: [461]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.012.001.08"]
---

# 11.4.2.2.2.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 461 to 461.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 461

```text
CodeName Name Definition
DIDB DirectDebit Limit not to be exceeded for direct debit
operations.
SPLC SingleCustomerDirectDebit Single direct debit payment limit not to
be exceeded by any single direct debit
transaction by a customer.
SPLF SingleFinancialInstitutionDirectDebit Single direct debit payment limit not to
be exceeded by any single direct debit
transaction initiated by a financial
institution.
TDLC TotalDailyCustomerDirectDebit Total daily payments limit for customer
direct debits not to be exceeded by the
total of all direct debit transactions
initiated by customers.
TDLF TotalDailyFinancialInstitutionDirectDebit Total daily payments limit for financial
institutions direct debits not to be
exceeded by the total of all direct debit
transactions initiated by financial
institutions.
UCDT UnsecuredCredit Limit is related to a cap amount granted
by a national central bank or a
settlement bank, but generally
unsecured outside of the market
infrastructure.
ACOL AutoCollateralisation Limit is related to a credit operation that
is or can be triggered when a buyer does
not have a sufficient amount of money to
settle a securities transaction in order to
improve its cash position for the next
settlement cycle. The credit provided can
be secured using securities already held
by the buyer ("collateral stocks") or the
securities that are being purchased
("collateral flows").
EXGT ExternalGuarantee Limit is related to a cap amount granted
by a national central bank or a
settlement bank.
11.4.2.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the limit, in a proprietary form.
Datatype: "Max35Text" on page 889
11.4.2.2.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.012.001.08 DeleteLimitV08
Cash Management - Maintenance 2024 - 2025 461 February 2025
```

