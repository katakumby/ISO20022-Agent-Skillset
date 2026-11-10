---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>", "3.4.3.1.1 LimitIdentification <LmtId>", "3.4.3.1.1.3 LimitCurrency <LmtCcy>"]
file_pages: [18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1.1.3 LimitCurrency <LmtCcy>

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 18 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 18

```text
CodeName Name Definition
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
3.4.3.1.1.3  LimitCurrency <LmtCcy>
Presence: [0..1]
Definition: Currency unit used to specify the limit amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 41
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.3.1.1.4  AccountOwner <AcctOwnr>
Presence: [1..1]
Definition: Owner of the account which is being queried.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 36 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 36
   LEI <LEI> [0..1] IdentifierSet 36
3.4.3.1.1.5  BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId>
Presence: [0..1]
Definition: Identification of the system member for which the limit is established.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 18 February 2025
```

