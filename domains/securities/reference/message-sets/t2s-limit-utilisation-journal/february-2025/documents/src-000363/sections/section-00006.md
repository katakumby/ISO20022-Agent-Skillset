---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["2 camt.064.001.01 LimitUtilisationJournalQueryV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.1 LimitType <LmtTp>"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.064.001.01"]
---

# 2.4.2.1 LimitType <LmtTp>

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
SearchCriteria <SchCrit> contains the following LimitUtilisationJournalSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LimitType <LmtTp> [0..*] CodeSet 6
   JournalActivityDate <JrnlActvtyDt> [1..1] Date 6
   AccountIdentification <AcctId> [0..1] ± 6
   LimitCurrency <LmtCcy> [0..1] CodeSet C1 7
   AccountOwner <AcctOwnr> [0..1] ± 7
   BilateralLimitCounterpartyIdentification
<BilLmtCtrPtyId>
[1..1] ± 7
2.4.2.1  LimitType <LmtTp>
Presence: [0..*]
Definition: Type of limit applied by the system at the present time.
Datatype: "LimitType4Code" on page 42
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
2.4.2.2  JournalActivityDate <JrnlActvtyDt>
Presence: [1..1]
Definition: Date upon which journal activity takes place.
Datatype: "ISODate" on page 43
2.4.2.3  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.064.001.01 LimitUtilisationJournalQueryV01
Target2-Securities - Limit Utilisation Journal 6 February 2025
```

