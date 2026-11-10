---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["5 camt.064.001.01 LimitUtilisationJournalQueryV01", "5.4 Message Building Blocks", "5.4.2 SearchCriteria <SchCrit>", "5.4.2.1 LimitType <LmtTp>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.064.001.01"]
---

# 5.4.2.1 LimitType <LmtTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
SearchCriteria <SchCrit> contains the following LimitUtilisationJournalSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitType <LmtTp> [0..*] CodeSet 70
   JournalActivityDate <JrnlActvtyDt> [1..1] Date 70
   AccountIdentification <AcctId> [0..1] ± 70
   LimitCurrency <LmtCcy> [0..1] CodeSet C1 71
   AccountOwner <AcctOwnr> [0..1] ± 71
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[1..1] ± 71
5.4.2.1  LimitType <LmtTp>
Presence: [0..*]
Definition: Type of limit applied by the system at the present time.
Datatype: "LimitType4Code" on page 3261
CodeName Name Definition
EXGT ExternalGuarantee Limit is related to a cap amount granted
by a national central bank or a
settlement bank.
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
5.4.2.2  JournalActivityDate <JrnlActvtyDt>
Presence: [1..1]
Definition: Date upon which journal activity takes place.
Datatype: "ISODate" on page 3319
5.4.2.3  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.064.001.01 LimitUtilisationJournalQueryV01
Target2-Securities 70 August 2026
```

