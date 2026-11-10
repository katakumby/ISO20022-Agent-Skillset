---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.1 ClearingAccount <ClrAcct>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.1 ClearingAccount <ClrAcct>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
               Name <Nm> [0..1] Text 188
               Characteristic <Chrtc> [0..1] Text 188
             ContactPerson <CtctPrsn> [0..1] ± 188
           SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 189
     GrossAmount <GrssAmt> [0..1] ± 189
4.4.5.1  ClearingAccount <ClrAcct>
Presence: [0..1]
Definition: Identifies the clearing member account at the Central counterparty through which the trade
must be cleared (sometimes called position account).
ClearingAccount <ClrAcct> contains the following elements (see SecuritiesAccount18 on page 373
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 373
   Type <Tp> [1..1] CodeSet 373
   Name <Nm> [0..1] Text 373
4.4.5.2  ClearingSegment <ClrSgmt>
Presence: [0..1]
Definition: Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing counterparty's
clearing system. Indeed, Clearing Member Firms receive messages from the same system (same
sender) and this field allows them to know if the message is related to equities or derivatives.
ClearingSegment <ClrSgmt> contains one of the following elements (see
PartyIdentification253Choice on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
4.4.5.3  NonClearingMember <NonClrMmb>
Presence: [0..1]
Definition: Provides the identification for the non-clearing member.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 140
```

