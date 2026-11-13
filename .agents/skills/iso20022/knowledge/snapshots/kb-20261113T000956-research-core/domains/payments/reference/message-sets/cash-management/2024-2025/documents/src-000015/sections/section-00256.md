---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.2 SearchCriteria <SchCrit>", "8.4.2.2.2.2.3 DefaultLimitType <DfltLmtTp>", "8.4.2.2.2.2.3.2 Proprietary <Prtry>"]
file_pages: [379]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.2.3.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 379 to 379.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 379

```text
CodeName Name Definition
liquidity when clearing specific type of
payments.
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
8.4.2.2.2.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the limit, in a proprietary form.
Datatype: "Max35Text" on page 889
8.4.2.2.2.2.4  CurrentLimitType <CurLmtTp>
Presence: [0..*]
Definition: Type of limit applied by the system at the present time.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 379 February 2025
```

