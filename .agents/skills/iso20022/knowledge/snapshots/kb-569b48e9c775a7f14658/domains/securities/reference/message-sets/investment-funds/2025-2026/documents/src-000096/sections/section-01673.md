---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.8 InvestmentAccountDetails <InvstmtAcctDtls>", "46.4.5.8.5 AccountServicer <AcctSvcr>"]
file_pages: [2349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.8.5 AccountServicer <AcctSvcr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2349 to 2349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2349

```text
Definition: Party that legally owns the account.
OwnerIdentification <OwnrId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
46.4.5.8.5  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
46.4.5.8.6  OrderOriginatorEligibility <OrdrOrgtrElgblty>
Presence: [0..1]
Definition: Counterparties eligibility as defined by article 24 of the EU MiFID Directive applicable to
transactions executed by investment firms for eligible counterparties.
Datatype: "OrderOriginatorEligibility1Code" on page 5332
CodeName Name Definition
ELIG Eligible Eligible counterparty - MiFID
classification of counterparty. Eligible
customers are the most sophisticated
level of investor, able to opt out of some
the protections afforded by conduct of
business rules defined under MiFID.
RETL Retail Retail client - MiFID classification of
counterparty. Retail customers are the
least sophisticated level of investor.
PROF Professional Professional client - MiFID classification
of counterparty. Professional customers
are, for example, investment firms, credit
institutions, insurance companies.
46.4.5.8.7  SubAccountDetails <SubAcctDtls>
Presence: [0..1]
Definition: Sub-account of the master or omnibus account.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2349 May 2026
```

