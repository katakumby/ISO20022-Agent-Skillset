---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.1 MessageDefinition Functionality"]
file_pages: [1489, 1490]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1489 to 1490.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1489

```text
40 sese.043.001.02
PortfolioTransferCompletionV02
40.1 MessageDefinition Functionality
Scope
The PortfolioTransferCompletion message is sent by an executing party, for example, a (old) plan
manager (transferor), to the instructing party for example, a (new) plan manager (transferee), to confirm
that the transfer of financial instruments from the client's account at the old plan manager (transferor) to
the clients account at the new plan manager (transferee) has been completed.
Usage
The PortfolioTransferCompletion message is used to confirm one or more portfolio transfers for one
client.
The reference of each portfolio transfer completion is identified in ProductTransfer/
TransferCompletionIdentification. The reference of the original portfolio transfer as assigned by the
instructing party is specified in TransferInstructionReference. The message identification of the
PortfolioTransferInstruction message in which the portfolio transfers were conveyed may also be quoted
in RelatedReference but this is not recommended.
Outline
The PortfolioTransferCompletionV02 MessageDefinition is composed of 17 MessageBuildingBlocks:
A. MessageReference
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. PrimaryIndividualInvestor
Information identifying the primary individual investor, for example, name, address, social security
number and date of birth.
F. RegisteredHolder
Official registered holder information.
G. SecondaryIndividualInvestor
Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
H. OtherIndividualInvestor
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1489 May 2026
```

## File page 1490

```text
Information identifying the other individual investors, for example, name, address, social security
number and date of birth.
I. PrimaryCorporateInvestor
Information identifying the primary corporate investor, for example, name and address.
J. SecondaryCorporateInvestor
Information identifying the secondary corporate investor, for example, name and address.
K. OtherCorporateInvestor
Information identifying the other corporate investors, for example, name and address.
L. TransferorAccount
Identification of the account owned by the investor at the old plan manager (account servicer).
M. NomineeAccount
Account held in the name of a party that is not the name of the beneficial owner of the shares.
N. Transferee
Identification of the institution to which the financial instrument has been transferred. This may also
be known as the new plan manager.
O. ProductTransfer
Information about the portfolio and assets.
P. MarketPracticeVersion
Identifies the market practice to which the message conforms.
Q. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1490 May 2026
```

