---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.33 ClearingDetails <ClrDtls>", "4.4.5.4.33.4 TradeCounterpartyIdentification <TradCtrPtyId>", "4.4.5.4.33.4.3 DeliveringParties <DlvrgPties>"]
file_pages: [173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.33.4.3 DeliveringParties <DlvrgPties>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 173 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
TradeCounterpartyClearingMemberIdentification <TradCtrPtyClrMmbId> contains one of the
following elements (see PartyIdentification253Choice on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
4.4.5.4.33.4.3  DeliveringParties <DlvrgPties>
Presence: [0..1]
Definition: Provides details about the delivering parties involved in the settlement chain.
Impacted by: C8 DepositoryGuideline
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 173
```

